// Generate .webp siblings for every .png/.jpg under img/ that lacks one, plus
// an -800w variant for images wide enough that a smaller download helps on
// phones. Run with: npm run webp   (requires `npm install` for sharp)
// The build-time plugin (_plugins/webp_picture.rb) serves these via <picture
// srcset>, choosing between the two widths.
import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

const NARROW_WIDTH = 800;

const walk = (d) => fs.readdirSync(d, { withFileTypes: true }).flatMap((e) =>
  e.isDirectory() ? walk(path.join(d, e.name)) : [path.join(d, e.name)]);

async function makeWebp(f, out, resizeWidth) {
  if (fs.existsSync(out)) return 'skipped';
  const orig = fs.statSync(f).size;
  let img = sharp(f).rotate();
  if (resizeWidth) img = img.resize({ width: resizeWidth, withoutEnlargement: true });
  const buf = await img.webp({ quality: 80, effort: 5 }).toBuffer();
  if (!resizeWidth && buf.length >= orig * 0.85) return 'skipped'; // not worth it
  fs.writeFileSync(out, buf);
  return 'made';
}

let made = 0, skipped = 0;
for (const f of walk('img')) {
  if (!/\.(png|jpe?g)$/i.test(f)) continue;
  try {
    const full = f.replace(/\.(png|jpe?g)$/i, '.webp');
    const r1 = await makeWebp(f, full, null);
    r1 === 'made' ? made++ : skipped++;

    const meta = await sharp(f).metadata();
    if (meta.width > NARROW_WIDTH * 1.25) {
      const narrow = f.replace(/\.(png|jpe?g)$/i, `-${NARROW_WIDTH}w.webp`);
      const r2 = await makeWebp(f, narrow, NARROW_WIDTH);
      r2 === 'made' ? made++ : skipped++;
    }
  } catch (e) { console.error('skip', f, e.message); }
}
console.log(`webp: made ${made}, skipped ${skipped}`);
