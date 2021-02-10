#!/bin/sh
REPOADD = $1
git init
# Second create a .gitignore file to exclude all files that doesn't need to be
# included in the GIT project
cd ~/.
git add .
echo "==============================="
echo "Listing the status of local GIT"
echo "==============================="
git status
echo ""
echo "Setting up global user name and user email"
echo ""
git config --global user.name "mashanivas"
git config --global user.email "mashanivas@gmail.com"
echo ""
echo "Committing to local repository"
echo ""
git commit -m "Initial committ"
echo ""
echo "Getting status..."
echo ""
git status
echo ""
echo ""
echo "Enter your remote GIT repository URL"
echo ""
read URL
echo "Addming $REPOADD to $URL"
git remote add REPOADD URL
git push $REPOADD master

