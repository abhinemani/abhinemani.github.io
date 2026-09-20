# Two build-time HTML rewrites for local /img/ <img> tags:
#
# 1. Inject width/height attributes (read from the actual file) on any local
#    image that lacks them, so the browser can reserve layout space before
#    the image loads (prevents layout shift).
#
# 2. Wrap <img src="/img/*.png|jpg"> in a <picture> with WebP <source>s. When
#    an -800w.webp sibling exists alongside the full-size .webp, both are
#    offered via srcset so phones can fetch the smaller file.
#
# WebP files (full-size and -800w) are generated offline with
# `npm run webp` and committed alongside the originals; this hook only
# rewrites the rendered HTML to reference them.
require 'fastimage'

module WebpPicture
  DIM_IMG_RE = %r{<img\b(?<attrs>[^>]*?)\bsrc="(?<origin>https?://[^/"]+)?/img/(?<path>[^"?#]+\.(?:png|jpe?g|gif|webp))"(?<rest>[^>]*)>}i
  PICTURE_IMG_RE = %r{<img\b(?<attrs>[^>]*?)\bsrc="(?<origin>https?://[^/"]+)?/img/(?<path>[^"?#]+)\.(?<ext>png|jpe?g)"(?<rest>[^>]*)>}i
  NARROW_WIDTH = 800

  def self.add_dimensions(html, site)
    return html unless html.include?('/img/')
    html.gsub(DIM_IMG_RE) do
      m = Regexp.last_match
      full_tag = m[0]
      next full_tag if full_tag =~ /\bwidth=/i && full_tag =~ /\bheight=/i
      abs = File.join(site.source, 'img', m[:path])
      next full_tag unless File.exist?(abs)
      dims = FastImage.size(abs) rescue nil
      next full_tag unless dims
      w, h = dims
      rest = m[:rest].sub(%r{\s*/\s*\z}, '') # drop a trailing self-closing slash (kramdown emits <img ... />)
      %(<img#{m[:attrs]}src="#{m[:origin]}/img/#{m[:path]}"#{rest} width="#{w}" height="#{h}">)
    end
  end

  def self.rewrite(html, site)
    return html unless html.include?('/img/')
    html.gsub(PICTURE_IMG_RE) do
      m = Regexp.last_match
      webp_rel = File.join('img', "#{m[:path]}.webp")
      next m[0] unless File.exist?(File.join(site.source, webp_rel))
      next m[0] if m.pre_match =~ %r{<picture\b[^>]*>(?:(?!</picture>).)*\z}m # already inside <picture>

      img = %(<img#{m[:attrs]}src="#{m[:origin]}/img/#{m[:path]}.#{m[:ext]}"#{m[:rest]}>)
      narrow_rel = File.join('img', "#{m[:path]}-#{NARROW_WIDTH}w.webp")
      srcset = if File.exist?(File.join(site.source, narrow_rel))
        full_w = (FastImage.size(File.join(site.source, webp_rel)) rescue nil)&.first
        %(#{m[:origin]}/#{narrow_rel} #{NARROW_WIDTH}w#{full_w ? ", #{m[:origin]}/#{webp_rel} #{full_w}w" : ''})
      else
        "#{m[:origin]}/#{webp_rel}"
      end
      %(<picture><source type="image/webp" srcset="#{srcset}"#{srcset.include?('w,') || srcset.end_with?('w') ? %( sizes="(max-width: 800px) 100vw, 744px") : ''}>#{img}</picture>)
    end
  end
end

Jekyll::Hooks.register [:documents, :pages], :post_render do |doc|
  next unless doc.output_ext == '.html'
  doc.output = WebpPicture.add_dimensions(doc.output, doc.site)
  doc.output = WebpPicture.rewrite(doc.output, doc.site)
end
