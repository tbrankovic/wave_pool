# Wave Pool
A python waveform generator made for end of studies research project.
<img width="1439" alt="Screenshot 2024-02-16 at 8 04 52 PM" src="https://github.com/tbrankovic/wave_pool/assets/79591971/89bf7bf7-e847-4987-9ff2-0a07b9a2bf33">


## Running the project
To run the project, you can run `main.py`.

## Selecting output file
1. in `WaveformFrame.py`, in the save waveform file, you can change the output filepath:
```py
def save_waveform(self):
    ...
    # ensure the waveform_out directory exists
    output_dir = os.path.join(os.getcwd(), 'waveform_out')  # <-- CHANGE THIS
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, self.file_path_entry.get() + '.txt')

    generate_awg_file(self.y, output_file_path)  # <-- OR CHANGE THIS
```
2. The output filepath depends on your working directory, you can change it under the interpreter setting.

## Dependencies
| Package          | Type      |
|------------------|-----------|
| os               | built-in  |
| tkinter          | built-in  |
| customtkinter    | third-party |
| numpy            | third-party |

## Notes
- The output file of the generated waveform is made for the **AWG70000**.
- The project is far from optimized and user friendly.

## Known issues
- If you notice the window is not detecting the interactions, try moving the window.
  - Technical reason: The issue comes from adding interactive object in frame objects

