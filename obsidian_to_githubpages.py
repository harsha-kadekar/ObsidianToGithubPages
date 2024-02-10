#!/usr/bin/env python

import yaml
import os
import subprocess
import shutil
import frontmatter
import argparse

OBYDE_CONFIG_FILE_PATH="converter_config.yaml"

def convert_obsidian_to_github_pages():
    subprocess.run(["obyde", "-c", OBYDE_CONFIG_FILE_PATH])

def post_processing(github_pages_repo_local):
    post_output_path = os.path.join(github_pages_repo_local, "_posts")

    for root, dirs, files in os.walk(post_output_path):
        for file in files:
            print("Found file: " + file)
            post = frontmatter.load(os.path.join(root, file))
            if (str(post.metadata.get("layout", "")) == "page"):
                print("This is a page instead of a post, so moving it")
                shutil.move(os.path.join(root, file), os.path.join(github_pages_repo_local, str(post.metadata.get("title") + ".md").lower()))


def generate_obyde_config_path(obsidian_local_vault, github_pages_repo_local):
    blog_path = os.path.join(obsidian_local_vault, "Blog")
    conversion_yaml = {
            "vault": {
                    "path": blog_path,
                    "asset_path": os.path.join(blog_path, "assets"),
                    "excluded_subdirectories": ["drafts"]
                },
            "output": {
                    "post_output_path": os.path.join(github_pages_repo_local, "_posts"),
                    "asset_output_path": os.path.join(github_pages_repo_local, "assets"),
                    "relative_asset_path_prefix": "{{ site.blog_assets_location }}",
                    "post_link_jekyll": "jekyll"
                }
    }


    with open(OBYDE_CONFIG_FILE_PATH, "w") as f:
        yaml.dump(conversion_yaml, f, sort_keys=False)

def main():
    cli = argparse.ArgumentParser()
    cli.add_argument(
            "--obsidian_local_vault",
            required=True
            )
    cli.add_argument(
            "--github_pages_repo_local",
            required=True
            )

    args = cli.parse_args()

    obsidian_local_vault = args.obsidian_local_vault
    github_pages_repo_local = args.github_pages_repo_local

    print("Going to start with following arguments")
    print("Obsidian Local Vault Location: " + obsidian_local_vault)
    print("Github pages local repository Location: " + github_pages_repo_local)

    generate_obyde_config_path(obsidian_local_vault, github_pages_repo_local)
    convert_obsidian_to_github_pages()
    post_processing(github_pages_repo_local)

if __name__ == "__main__":
    main()
