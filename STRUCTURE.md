## Directory structure

Each capsule has its own directory, with each checklist being represented with a sub-directory containing a JSON-file.
Checklist project-names should use CamelCase, not spaces.

## File structure
### Main structure

| Field name    | Field type            | Description                                                                                      |
|---------------|-----------------------|--------------------------------------------------------------------------------------------------|
| checklistText | String                | Text of the checklist, as it will appear on the screen when run through. Use `\n` for a new line |
| Group         | String                | Tells you which group the checklist should appear in                                             |
| Images        | List\<ChecklistImage> | A list of images                                                                                 |
| Name          | String                | The name for the checklist as it will be shown to the user                                       |
| ProjectName   | String                | Same as the directory-name for the checklist                                                     |
| Side          | SideOption            | Which side of the checklist-menu the checklist appears on. 0 for XXX, 1 for YYY                  |
| SortPriority  | Integer               | Used to determine which order the checklist should appear in on the menu                         |
| Spacecraft    | Spacecraft            | Specifies the spacecraft this is for                                                             |
| Steps         | List\<Step>           | List of steps to tell the user to take                                                           |


#### ChecklistImage

Attribute | Description
----------|------------
Name      | This is the "name" of the image
Position  | Where to place the image (X and Y). Note: This is absolute within the checklist interface.
Size      | This is the size (height and width) to scale the image to while preserving height/width ratio

#### SideOption

n | Description
--|----------
0 | Left
1 | Right

#### Spacecraft


n | Description
--|----------
0 | Apollo CM
1 | Apollo LM
2 | Gemini
3 | Mercury

#### Step

| Field name | Field type | Description                                                      |
|------------|------------|------------------------------------------------------------------|
| Program    | Spacecraft | Specifies the spacecraft this step is for                        |
| Type       | TypeOption | Indicates what sort of switch is referenced. 0 for a manual step |
| SetID      | Integer    | Denotes the ID of the switch, fuse, ... this step applies to     |
| ToPosID    | Integer    | Denotes the position the switch etc should be set to             |
| Text       | String     | The text that goes with the step                                 |

#### TypeOption
| n | Description                                              |
|---|----------------------------------------------------------|
| 0 | "Manual" (As in the pilot will have to do this manually) |
| 1 | Switch                                                   |
| 2 | Circuit breaker                                          |
| 3 | Selector                                                 |
| 4 | Button                                                   |
| 5 | Handle                                                   |
| 6 | ExpButton                                                |

## Formatting

Some fields supports tags for formatting. For example, `<size=72>BIG TEXT</size>` makes "BIG TEXT" appear in 72 pixels high.
