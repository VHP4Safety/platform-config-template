# Virtual X Platform configuration

The content from which the [Virtual X Platform](https://github.com/YOUR-ORG/virtual-x-platform) is made: its
glossary, its tools and methods, and its use cases. This repository is a template, derived from three repositories
of [VHP4Safety](https://github.com/VHP4Safety) (`glossary`, `cloud` and `ui-casestudy-config`), and ships with
demo content, Lorem Ipsum style.

| Folder | Content | Demo content |
|---|---|---|
| [`glossary/`](glossary) | the common vocabulary, including the *process flow steps* | three process flow steps (Lorem, Ipsum, Dolor), a few terms, one chemical |
| [`cloud/`](cloud) | the catalog of tools and methods | one demo tool, one demo method |
| [`casestudies/`](casestudies) | the use cases and their questions | one demo use case with one question |

Each folder has a README with the details.

## How the platform uses this repository

- The **glossary** is pinned in the platform (`python -m linkeddata pin glossary`), and read again each week. Its
  terms have addresses on the website of this repository, such as
  `https://YOUR-ORG.github.io/virtual-x-platform-config/glossary#VXP0000004`.
- The **tools, methods and use cases** are read once, when the platform is launched. After the launch, they are
  changed in the editor of the platform. This repository stays the place where users request new terms, tools and
  methods, with the issue forms.

## The website

GitHub Pages serves one website for this repository:

| Address | Content | Made from |
|---|---|---|
| `https://YOUR-ORG.github.io/virtual-x-platform-config/` | the home page | [`site-index.md`](site-index.md) |
| `…/glossary/` | the glossary, with its terms in HTML+RDFa, and `glossary.owl` | `glossary/index.md`, `glossary/glossary.owl` |
| `…/cloud/` | the tool and method catalog | `cloud/docs/` |

## GitHub Actions

The workflows in [`.github/workflows/`](.github/workflows) generate files from the content and commit them:

| Workflow | When | What |
|---|---|---|
| `update_md.yml`, `extract.yml` | a change in `glossary/templates/` | `glossary/index.md`, then `glossary/glossary.owl` |
| `assign-id.yml`, `cleanup-id.yml` | a term request issue is opened or closed | reserves or frees a glossary identifier |
| `create-markdown-v2.yml`, `generate_service_index.yml` | a change in `cloud/docs/service/` | the catalog pages and `cloud/cap/service_index.json` |
| `create_method_json_pr.yml` | a method request issue gets a `method` label | a pull request with the method JSON |
| `generate_method_*.yml` | a change in `cloud/docs/methods/` | the method pages, index and `cloud/cap/methods_index.json` |
| `jekyll-gh-pages.yml` | a push, or after the workflows above | the website |

The issue forms are in [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE): a glossary term request, a new tool, and a
new method.

## Set it up

1. Replace `YOUR-ORG` everywhere with your GitHub organization (see the tutorial of the template).
2. Push the repository to GitHub as `YOUR-ORG/virtual-x-platform-config`.
3. Allow GitHub Actions to commit the files they generate: *Settings → Actions → General → Workflow permissions →
   Read and write permissions*, and tick *Allow GitHub Actions to create and approve pull requests*.
4. Serve the website: *Settings → Pages → Source: GitHub Actions*.

To generate the files on your own computer, use `make content` in the folder of the template.

## License

This work is licensed under [CC-BY 4.0 International](LICENSE.md). The scripts and workflows are derived from the
VHP4Safety repositories [glossary](https://github.com/VHP4Safety/glossary), [cloud](https://github.com/VHP4Safety/cloud)
and [ui-casestudy-config](https://github.com/VHP4Safety/ui-casestudy-config).
