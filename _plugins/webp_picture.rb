# Wraps <img> tags that point at /img/*.png|jpg in a <picture> element with a
# WebP <source> when a sibling .webp exists next to the original file.
# WebP files are generated offline (see README) and committed alongside the
# originals; this hook only rewrites the rendered HTML.
module WebpPicture
  IMG_RE = %r{<img\b(?<attrs>[^>]*?)\bsrc="(?<origin>https?://[^/"]+)?/img/(?<path>[^"?#]+)\.(?<ext>png|jpe?g)"(?<rest>[^>]*)>}i

  def self.rewrite(html, site)
    return html unless html.include?('/img/')
    html.gsub(IMG_RE) do
      m = Regexp.last_match
      webp_rel = File.join('img', "#{m[:path]}.webp")
      next m[0] unless File.exist?(File.join(site.source, webp_rel))
      next m[0] if m.pre_match =~ %r{<picture\b[^>]*>(?:(?!</picture>).)*\z}m # already inside <picture>
      img = %(<img#{m[:attrs]}src="#{m[:origin]}/img/#{m[:path]}.#{m[:ext]}"#{m[:rest]}>)
      %(<picture><source type="image/webp" srcset="#{m[:origin]}/#{webp_rel}">#{img}</picture>)
    end
  end
end

Jekyll::Hooks.register [:documents, :pages], :post_render do |doc|
  next unless doc.output_ext == '.html'
  doc.output = WebpPicture.rewrite(doc.output, doc.site)
end
