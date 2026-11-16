# Virtual X Platform Glossary

Template for the glossary of a Virtual X Platform: the common vocabulary of the
project. It is derived from the [VHP4Safety glossary](https://github.com/VHP4Safety/glossary)
and ships with demo content: three demo *process flow steps* (Lorem, Ipsum, Dolor),
a few Lorem Ipsum terms, a demo tool and method, and one chemical.

The glossary is published in two forms:

* [`index.md`](index.md): the human-readable page (served by GitHub Pages at `https://YOUR-ORG.github.io/virtual-x-platform-config/glossary/`)
* [`glossary.owl`](glossary.owl): the machine-readable OWL version (Turtle), which the platform reads

Both files are **generated**: do not edit them by hand.

## Why the glossary comes first

The tools, methods, use cases and the platform refer to terms in this glossary by their IRI,
`https://YOUR-ORG.github.io/virtual-x-platform-config/glossary#VXP0000004`:

* tools and methods use a *Process Flow Step* IRI as their `stage`
* use cases list the process flow steps of each question
* the platform reads the process flow steps from `glossary.owl`, and highlights
  glossary terms in its pages

A term becomes a process flow step when its label ends with
`(<i>Process Flow Step</i>)`, see [`templates/process_flow.tsv`](templates/process_flow.tsv).

## Make it yours

1. Replace `YOUR-ORG` everywhere with your GitHub organization (see the tutorial in the template root).
2. Optionally pick your own identifier prefix instead of `VXP` (in `templates/`, `scripts/`, and the workflows `assign-id.yml` and `cleanup-id.yml` in `.github/workflows/` of the repository).
3. Edit the text around the tables in [`index_template.md`](index_template.md).
4. Replace the demo terms in [`templates/`](templates) with your own.
5. Enable GitHub Pages for the repository (see the [README of the repository](../README.md)), so the glossary is
   served at `https://YOUR-ORG.github.io/virtual-x-platform-config/glossary/`.

## Adding terms

Terms live in tab-separated tables in [`templates/`](templates), one row per term.

| Column | Meaning |
|---|---|
| `ID` | unique identifier, `VXP` plus seven digits |
| `Term` | the label |
| `Abbreviation` | optional |
| `Definition` | the definition; may contain HTML |
| `ref` | optional, comma-separated URLs of references |
| `related_to` | optional, IRI of a related term |
| `synonyms`, `see_also` | optional, comma-separated IDs of other terms |
| `SMILES` | optional, depicted as a chemical structure |

Users can request a term with the issue template; a GitHub Action then reserves
the next free identifier and comments it on the issue.

### Adding a new section

1. Add a new table to [`templates/`](templates), e.g. `organizations.tsv`.
2. Add a header and placeholder to [`index_template.md`](index_template.md), e.g. `${organizations}`.
3. Register the placeholder and file name in the `sections` dictionary of
   [`scripts/template_to_md.py`](scripts/template_to_md.py).

## How the files are generated

| Step | Tool | GitHub Action |
|---|---|---|
| `templates/*.tsv` + `index_template.md` → `index.md` (HTML tables with [RDFa](https://rdfa.info/docs)) | `scripts/template_to_md.py` | `update_md.yml` |
| `index.md` → `glossary.owl` | `extractOWL.groovy` | `extract.yml` |

To run this locally (needs Python with pandas, pandoc, and Groovy):

```shell
python3 scripts/template_to_md.py
pandoc index.md -f gfm -t html5 -s -M lang=en-US -M pagetitle="Glossary" -o /tmp/glossary.html
groovy extractOWL.groovy /tmp/glossary.html > glossary.owl
```

Each row of a table becomes an OWL class:

```html
<tr id="VXP0000007" about="https://YOUR-ORG.github.io/virtual-x-platform-config/glossary#VXP0000007" typeof="owl:Class">
  <td><span property="rdfs:label">Lorem ipsum</span></td>
  <td property="ncit:C42610">LI</td>
  <td><span property="dc:description">Placeholder text ...</span></td>
</tr>
```

## License

This work is licensed under [CC-BY 4.0 International](../LICENSE.md). The scripts and
workflows are derived from the [VHP4Safety glossary](https://github.com/VHP4Safety/glossary).
