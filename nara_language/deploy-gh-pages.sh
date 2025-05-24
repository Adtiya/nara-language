#!/bin/bash
# GitHub Pages Deployment Script for NĀRA

echo "🚀 Deploying NĀRA site to GitHub Pages..."
git checkout --orphan gh-pages
git --work-tree=nara_launch_site add --all
git --work-tree=nara_launch_site commit -m 'Deploy NĀRA site'
git push origin gh-pages --force
git checkout -f main
git branch -D gh-pages
echo "🌐 Deployed to https://<your-username>.github.io/<repo-name>/"
