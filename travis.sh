#!/usr/bin/env bash

GIT_COMMIT_MESSAGE="upate latest file"
GIT_REPO="cr4ftsm4n/my-youtube-downloader"
GIT_BRANCH="master"

git checkout "${GIT_BRANCH}"

python main.py

git add latest_id
git status
git -c "commit.gpgsign=false" \
    -c "user.name=${GIT_NAME}" \
    -c "user.email=${GIT_EMAIL}" \
    commit -m "${GIT_COMMIT_MESSAGE}"

# push changes
# always return true so that the build does not fail if there are no changes
git push "https://x-token:${GITHUB_TOKEN}@github.com/${GIT_REPO}" "${GIT_BRANCH}" || true
