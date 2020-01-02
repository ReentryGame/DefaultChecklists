## Directory structure

Each capsule has its own directory, with each checklist being represented with a sub-directory containing a JSON-file.
Checklist project-names should use CamelCase, not spaces.

## File structure
### Main structure

| Field name    | Field type  | Description                                                                                      |
|---------------|-------------|--------------------------------------------------------------------------------------------------|
| checklistText | String      | Text of the checklist, as it will appear on the screen when run through. Use `\n` for a new line |
| Group         | String      | Tells you which group the checklist should appear in                                             |
| Images        | List<???>   | A list of images???                                                                              |
| Name          | String      | The name for the checklist as it will be shown to the user                                       |
| ProjectName   | String      | Same as the directory-name for the checklist                                                     |
| Side          | Integer      | Which side of the checklist-menu the checklist appears on. 0 for XXX, 1 for YYY                  |
| SortPriority  | Integer      | Used to determine which order the checklist should appear in on the menu                         |
| Spacecraft    | Integer      | 1 for XXX, 2 for XXX, 3 for Mercury                                                              |
| Steps         | List\<Step> | List of steps to tell the user to take                                                           |

### Step

| Field name | Field type | Description                                                  |
|------------|------------|--------------------------------------------------------------|
| Program    | Integer    | ???                                                          |
| Type       | Integer    | ???                                                          |
| SetID      | Integer    | Denotes the ID of the switch, fuse, ... this step applies to |
| ToPosID    | Integer    | Denotes the position the switch etc should be set to         |
| Text       | String     | The text that goes with the step                             |

## Formatting

Some fields supports tags for formatting. For example, `<size=72>BIG TEXT</size>` makes "BIG TEXT" appear in 72 pixels high.