# Virtual X Platform use cases

Template for the folder that defines the **use cases** shown on a Virtual X
Platform. It is derived from the
[VHP4Safety case study configuration](https://github.com/VHP4Safety/ui-casestudy-config)
and ships with demo content: one demo use case with one question.

The platform code calls a use case a *case study* and a use case question a
*regulatory question*; that is why these names appear in file names, URLs, and
JSON values.

## Files

| File | Purpose |
|---|---|
| [`ro-crate-metadata.json`](ro-crate-metadata.json) | [RO-Crate](https://www.researchobject.org/ro-crate/) that lists the use cases; the platform reads this file first |
| [`demo_content.json`](demo_content.json) | the content of the demo use case |
| [`Images/`](Images) | figures used in the content |

## How the platform uses these files

The platform reads these files **once**, when it is launched (`python -m linkeddata launch`), and stores each use
case as a record. After the launch, use cases are changed in the record editor of the platform (`/admin/`), not
here: later changes to this folder are not read again. This folder is the starting point, and a readable
copy of the first version of the use cases.

1. The platform lists the files to read in its `linkeddata/launch/casestudies.yaml`: this RO-Crate and the content
   file of each use case, by its identifier.
2. From `ro-crate-metadata.json` it takes the `name`, `description` and `keywords` of each use case, by the
   `identifier`: the slug in the address of the use case (`/casestudies/demo`).
3. From the content file it makes the pages of the use case: the use case, its questions
   (`/casestudies/demo/Q1`), and the steps below them (`/casestudies/demo/Q1/lorem`).

## Structure of a use case

The content JSON has one object per level of the page. Each deeper level is
keyed by the `value` of the buttons chosen in the levels before it.

| Key | Shows | Keyed by |
|---|---|---|
| `step1Contents` | the use case and its `questions` | – |
| `step2Contents` | the process flow `steps` of a question | question |
| `step3Contents` | the workflow `steps` or `tools` of a process flow step | question → step |
| `step4Contents` … `step6Contents` | optional deeper levels | question → step → … |

Every level has a `navTitle`, a `navDescription`, a list of buttons (`questions`,
`steps`, or `tools`), and `content`: a list of sections (`section` is the
heading, `description` the text, which may contain HTML).

A button has these fields:

| Field | Meaning |
|---|---|
| `label` | text on the button |
| `description` | optional second line on the button |
| `value` | key of the next level; also used in the URL |
| `type` | `regulatory-question`, `process-flow-step`, `workflow step`, `workflow substep`, `tool`, or `data`; sets the colour and behaviour |
| `state` | optional, `disabled` shows the button greyed out |
| `id` | for a `tool`: the tool ID, linking to `/tools/<id>`; for `data`: the dataset ID, linking to `/data/<id>`; for a question: its code in the catalogues (see below) |
| `route` | optional, for a `tool` button: `methods` links to `/methods/<id>` instead |
| `glossaryUrl` | for a process flow step: the term in the glossary |

## Links to the glossary, the tools and the platform

* **Glossary:** the `glossaryUrl` of a process flow step is the address of a
  *Process Flow Step* term on the glossary website, such as
  `https://YOUR-ORG.github.io/virtual-x-platform-config/glossary/#VXP0000004`. The platform accepts only the
  process flow steps of its pinned glossary.
* **Tools and methods:** a question has a code in the tool and method catalogues:
  `1a` for use case 1, question a. Tools mark the questions they are used for in
  their `regulatory-question` field (`"1a": "true"`), and methods in their
  *Use case question* field. The platform maps each code to the address of its
  question in `linkeddata/launch/casestudies.yaml`
  (`reg_q_1a: casestudies/demo/Q1`). The `id` of a question in this folder
  records the same code, for readers.
* **Tools and methods:** the `id` of a `tool` button is the ID of a tool or method
  in the [`cloud/`](../cloud) folder.

## Make it yours

1. Replace `YOUR-ORG` everywhere with your GitHub organization (see the tutorial in the template root).
2. Copy `demo_content.json` to `<slug>_content.json` and write your use case.
3. Add a `File` entry for it to `ro-crate-metadata.json` (and to `hasPart` of the root dataset), and remove the demo entry.
4. Put figures in `Images/` and refer to them with their raw GitHub URL, as the demo content does.
5. In the platform repository, list the content file and the codes of its questions in
   `linkeddata/launch/casestudies.yaml`, before the launch.

## License

This work is licensed under [CC-BY 4.0 International](../LICENSE.md).
