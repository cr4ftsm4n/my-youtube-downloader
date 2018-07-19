#!/usr/bin/env bash

GIT_COMMIT_MESSAGE="upate latest file"
GIT_REPO="cr4ftsm4n/my-youtube-downloader"
GIT_BRANCH="master"

python main.py

git status
git add latest_id
git -c "commit.gpgsign=false" \
    -c "user.name=${GIT_NAME}" \
    -c "user.email=${GIT_EMAIL}" \
    commit -m "${GIT_COMMIT_MESSAGE}"
git push "https://x-token:${GITHUB_TOKEN}@github.com/${GIT_REPO}" "${GIT_BRANCH}"
