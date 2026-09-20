// Generate .webp siblings for every .png/.jpg under img/ that lacks one.
// Run with: npm run webp   (requires `npm install` for sharp)
// The build-time plugin (_plugins/webp_picture.rb) serves them via <picture>.
import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

const walk = (d) => fs.readdirSync(d, { withFileTypes: true }).flatMap((e) =>
  e.isDirectory() ? walk(path.join(d, e.name)) : [path.join(d, e.name)]);

let made = 0, skipped = 0;
for (const f of walk('img')) {
  if (!/\.(png|jpe?g)$/i.test(f)) continue;
  const out = f.replace(/\.(png|jpe?g)$/i, '.webp');
  if (fs.existsSync(out)) { skipped++; continue; }
  try {
    const orig = fs.statSync(f).size;
    const buf = await sharp(f).rotate().webp({ quality: 80, effort: 5 }).toBuffer();
    if (buf.length < orig * 0.85) { fs.writeFileSync(out, buf); made++; } else skipped++;
  } catch (e) { console.error('skip', f, e.message); }
}
console.log(`webp: made ${made}, skipped ${skipped}`);
