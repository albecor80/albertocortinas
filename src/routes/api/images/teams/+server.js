import fs from 'fs';
import path from 'path';

export async function GET() {
  const directoryPath = path.resolve('static/img/equips');
  try {
    const files = fs.readdirSync(directoryPath).filter(file => /\.(jpg|jpeg|png|gif|webp)$/i.test(file));
    return new Response(JSON.stringify(files), { status: 200 });
  } catch (err) {
    return new Response('Error reading directory', { status: 500 });
  }
}
