import fs from 'fs';
import path from 'path';

export async function load() {
  const articlesDir = path.resolve('src/routes/articles');

  let articleFolders = [];
  try {
    articleFolders = fs.readdirSync(articlesDir)
      .filter(folder => fs.lstatSync(path.join(articlesDir, folder)).isDirectory());
  } catch (error) {
    console.error('Error reading articles directory:', error);
  }

  const articles = articleFolders.map(folder => ({
    id: folder,
    title: `Article ${folder}`
  }));
  return { articles };  // Ensure this is returned properly
}