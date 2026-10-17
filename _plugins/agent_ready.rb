# Build-time output for AI agents and LLM crawlers:
#
# 1. Markdown sidecars. Every post, lesson, portfolio case study and Markdown
#    page gets a clean .md copy next to its HTML (/blog/2026/09/21/Trust/ ->
#    /blog/2026/09/21/Trust.md), following the llmstxt.org convention. Inline
#    <style>/<script> blocks (interactive charts) and HTML comments are
#    stripped, and each <figure> becomes a short Markdown paragraph: its
#    title, its data-md-summary attribute (or, failing that, its subtitle and
#    fallback text), and its caption. An <iframe> becomes a line such as
#    "Embedded video: <url>", newsletter cards become a bulleted list of
#    links, and forms and layout <div>/<span>/<section> wrappers are dropped.
#    Each document's sidecar URL is exposed as `page.markdown_url`
#    so head.html and llms.txt can link to it. Every remaining page gets a
#    short stub (title, description, canonical URL), so any URL ending in /
#    has a .md sibling.
#
# 2. /llms-full.txt: every sidecar concatenated, newest first.
#
# 3. Agent Skills discovery (Cloudflare RFC v0.2.0). Each _agent_skills/<name>/
#    SKILL.md is copied byte-for-byte to /.well-known/agent-skills/<name>/
#    SKILL.md, and /.well-known/agent-skills/index.json is written with each
#    file's sha256 digest. The sources live in an underscore folder so Jekyll
#    doesn't eat their YAML front matter.
#
# /llms.txt itself is a hand-curated Liquid page at the site root.
require 'cgi'
require 'digest'
require 'json'
require 'fileutils'

module AgentReady
  SKILLS_SRC = '_agent_skills'
  SKILLS_DEST = '.well-known/agent-skills'
  SKILLS_SCHEMA = 'https://schemas.agentskills.io/discovery/0.2.0/schema.json'
  MARKDOWN_PAGES = %w[talks.md community.md].freeze

  # Raw Markdown captured right after the site is read, before Jekyll renders
  # it, keyed by relative path.
  @sources = {}
  class << self; attr_reader :sources; end

  def self.documents(site)
    docs = site.posts.docs + %w[lessons portfolio].flat_map { |c| site.collections[c]&.docs || [] }
    pages = site.pages.select { |p| MARKDOWN_PAGES.include?(p.relative_path) }
    (docs + pages).reject { |d| d.data['published'] == false }
  end

  def self.markdown_url(url)
    url = url.sub(%r{/index\.html\z}, '/')
    "#{url.chomp('/')}.md"
  end

  def self.clean(body, site)
    body
      .gsub(/\{\{\s*site\.url\s*\}\}/, site.config['url'].to_s)
      .gsub(/\]\(\/(?!\/)/, "](#{site.config['url']}/")
      .gsub(/<!--.*?-->/m, '')
      .gsub(%r{<style\b.*?</style>}mi, '')
      .gsub(%r{<script\b.*?</script>}mi, '')
      .gsub(%r{<figure\b.*?</figure>}mi) { |fig| figure(fig) }
      .gsub(%r{<iframe\b[^>]*>.*?</iframe>}mi) { |frame| embed(frame) }
      .gsub(%r{<div class="newsletter-grid".*?</div>\s*</div>}mi) { |grid| cards(grid) }
      .gsub(%r{<form\b.*?</form>}mi, '')
      .gsub(%r{</?(?:div|span|section)\b[^>]*>}i, '')
      .gsub(/^[ \t]+(?=<)/, '')
      .gsub(/[ \t]+$/, '')
      .gsub(/\n{3,}/, "\n\n")
      .strip
  end

  # Inline HTML to plain Markdown text: links become [text](href), every
  # other tag is dropped and entities are decoded.
  def self.text(html)
    CGI.unescapeHTML(html.to_s
      .gsub(%r{<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>}mi, '[\\2](\\1)')
      .gsub(/<[^>]+>/, ''))
      .gsub(/\s+/, ' ').strip
  end

  # An <iframe> (video, slide deck, PDF, interactive chart) becomes a single
  # line naming what it is and where to find it.
  def self.embed(html)
    src = CGI.unescapeHTML(html[/\bsrc="([^"]*)"/i, 1].to_s).strip
    return '' if src.empty?

    kind = case src
           when /youtube\.com|youtu\.be|vimeo\.com/ then 'video'
           when /canva\.com/ then 'slides'
           when /\.pdf\b/i then 'PDF'
           else 'content'
           end
    "\n\nEmbedded #{kind}: #{src}\n\n"
  end

  # A newsletter-grid of cards becomes a bulleted list of links.
  def self.cards(html)
    items = html.scan(%r{<div class="newsletter-card"[^>]*>(.*?)</div>}mi).map do |(card)|
      link = text(card[%r{<strong>(.*?)</strong>}mi, 1])
      description = text(card[%r{<small>(.*?)</small>}mi, 1])
      "- #{link}#{": #{description}" unless description.empty?}"
    end
    "\n\n#{items.join("\n")}\n\n"
  end

  def self.figure(html)
    open_tag = html[/\A<figure\b[^>]*>/i]
    title = text(html[%r{<p class="tg-title">(.*?)</p>}m, 1])
    summary = CGI.unescapeHTML(open_tag[/data-md-summary="([^"]*)"/, 1].to_s).strip
    if summary.empty?
      summary = [html[%r{<p class="tg-sub">(.*?)</p>}m, 1], html[%r{<canvas\b[^>]*>(.*?)</canvas>}m, 1]]
                .map { |part| text(part) }.reject(&:empty?).map { |part| part.sub(/(?<![.!?])\z/, '.') }.join(' ')
    end
    caption = text(html[%r{<figcaption\b[^>]*>(.*?)</figcaption>}m, 1])
    out = +''
    out << "**Chart: #{title.sub(/(?<![.!?])\z/, '.')}** " unless title.empty?
    out << summary
    out << " *#{caption}*" unless caption.empty?
    "\n#{out.strip}\n"
  end

  def self.sidecar(doc, site)
    d = doc.data
    meta = ["URL: #{site.config['url']}#{doc.url.sub(%r{index\.html\z}, '')}"]
    meta << "Published: #{d['date'].strftime('%Y-%m-%d')}" if d['date'].respond_to?(:strftime) && doc.respond_to?(:collection) && doc.collection&.label == 'posts'
    meta << "Author: #{d['author'] || site.config.dig('owner', 'name')}"
    tags = Array(d['tags']).reject(&:nil?)
    meta << "Tags: #{tags.join(', ')}" unless tags.empty?

    out = +"# #{CGI.unescapeHTML(d['title'].to_s).strip}\n\n"
    out << "> #{CGI.unescapeHTML(d['subhead'].to_s).gsub(/\s+/, ' ').strip}\n\n" unless d['subhead'].to_s.strip.empty?
    out << meta.join("\n") << "\n\n---\n\n"
    out << clean(sources.fetch(doc.relative_path, ''), site) << "\n"
  end

  # Every other page ending in / gets a short stub, so that "add .md to any
  # URL" never 404s. The Cloudflare rule that serves Markdown to agents sending
  # `Accept: text/markdown` relies on this. Redirect pages point to their target.
  def self.write_stubs(site)
    Dir[File.join(site.dest, '**', 'index.html')].each do |html_path|
      rel = html_path.delete_prefix(site.dest).delete_suffix('index.html')
      md_path = File.join(site.dest, rel == '/' ? '/index.md' : "#{rel.chomp('/')}.md")
      next if File.exist?(md_path)

      html = File.read(html_path)
      canonical = html[/<link rel="canonical" href="([^"]+)"/, 1] || "#{site.config['url']}#{rel}"
      if html.include?('http-equiv="refresh"')
        target_md = File.join(site.dest, "#{canonical.delete_prefix(site.config['url']).chomp('/')}.md")
        alt = File.exist?(target_md) ? " (Markdown: #{canonical.chomp('/')}.md)" : ''
        write(md_path, "# Moved\n\nThis page has moved to #{canonical}#{alt}\n")
        next
      end
      title = CGI.unescapeHTML(html[%r{<title>([^<]*)</title>}, 1].to_s).sub(/ \| #{Regexp.escape(site.config['title'])}\z/, '').strip
      description = CGI.unescapeHTML(html[/<meta name="description" content="([^"]*)"/, 1].to_s).strip
      out = +"# #{title}\n\n"
      out << "> #{description}\n\n" unless description.empty?
      out << "URL: #{canonical}\n\n---\n\n"
      out << "This page has no Markdown version of its text; read it at #{canonical}. " \
             "For an index of all of Abhi Nemani's writing in Markdown, see #{site.config['url']}/llms.txt\n"
      write(md_path, out)
    end
  end

  def self.write(path, content)
    FileUtils.mkdir_p(File.dirname(path))
    File.write(path, content)
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  AgentReady.sources.clear
  AgentReady.documents(site).each do |d|
    d.data['markdown_url'] = AgentReady.markdown_url(d.url)
    AgentReady.sources[d.relative_path] = d.content.dup
  end
end

# {{ page.title | decode_entities }}: turns &#x3A; and friends back into text.
module AgentReadyFilters
  def decode_entities(input)
    CGI.unescapeHTML(input.to_s)
  end
end
Liquid::Template.register_filter(AgentReadyFilters)

Jekyll::Hooks.register :site, :post_write do |site|
  docs = AgentReady.documents(site)

  sidecars = docs.map do |doc|
    md = AgentReady.sidecar(doc, site)
    AgentReady.write(File.join(site.dest, doc.data['markdown_url']), md)
    [doc, md]
  end

  posts_first = sidecars.sort_by { |doc, _| doc.data['date'].respond_to?(:to_time) ? -doc.data['date'].to_time.to_i : 0 }
  full = +"# #{site.config['title']}: full text\n\n"
  full << "> Every essay, Public Innovation Academy lesson and portfolio case study on #{site.config['url']}, as Markdown. Curated index: #{site.config['url']}/llms.txt\n\n"
  full << posts_first.map { |_, md| md }.join("\n\n---\n\n")
  AgentReady.write(File.join(site.dest, 'llms-full.txt'), full)
  AgentReady.write_stubs(site)

  skills = Dir[File.join(site.source, AgentReady::SKILLS_SRC, '*', 'SKILL.md')].sort.map do |src|
    name = File.basename(File.dirname(src))
    bytes = File.binread(src)
    description = bytes[/\A---\s*\n.*?^description:\s*(.+?)\s*$/m, 1].to_s.delete_prefix('"').delete_suffix('"')
    url = "/#{AgentReady::SKILLS_DEST}/#{name}/SKILL.md"
    FileUtils.mkdir_p(File.dirname(File.join(site.dest, url)))
    File.binwrite(File.join(site.dest, url), bytes)
    { 'name' => name, 'type' => 'skill-md', 'description' => description,
      'url' => url, 'digest' => "sha256:#{Digest::SHA256.hexdigest(bytes)}" }
  end
  index = { '$schema' => AgentReady::SKILLS_SCHEMA, 'skills' => skills }
  AgentReady.write(File.join(site.dest, AgentReady::SKILLS_DEST, 'index.json'), JSON.pretty_generate(index) + "\n")
end
