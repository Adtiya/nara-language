
// nara-bot.js — GitHub Bot for Reviewing .nara Pull Requests
const core = require('@actions/core');
const github = require('@actions/github');

async function run() {
  try {
    const token = core.getInput('GITHUB_TOKEN');
    const octokit = github.getOctokit(token);
    const context = github.context;

    const pr = context.payload.pull_request;
    const repo = context.repo;

    if (!pr) {
      core.info("No pull request found.");
      return;
    }

    const files = await octokit.rest.pulls.listFiles({
      owner: repo.owner,
      repo: repo.repo,
      pull_number: pr.number,
    });

    const comments = [];

    for (const file of files.data) {
      if (file.filename.endsWith(".nara")) {
        const content = await fetch(file.raw_url).then(res => res.text());
        if (!content.includes("पुरुषः")) {
          comments.push({
            path: file.filename,
            body: "⚠️ This `.nara` file is missing an agent declaration (`पुरुषः`).",
            line: 1,
          });
        }
        if (!content.includes("कर्मे")) {
          comments.push({
            path: file.filename,
            body: "⚠️ This `.nara` file is missing a task block (`कर्मे`).",
            line: 1,
          });
        }
      }
    }

    for (const comment of comments) {
      await octokit.rest.pulls.createReviewComment({
        ...repo,
        pull_number: pr.number,
        commit_id: pr.head.sha,
        path: comment.path,
        body: comment.body,
        line: comment.line,
        side: 'RIGHT',
      });
    }

    if (comments.length === 0) {
      core.info("✅ All .nara files passed basic validation.");
    }

  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
