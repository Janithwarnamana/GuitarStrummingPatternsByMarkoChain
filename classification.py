time_signatures = ['3/4', '4/4']
ts_input = time_signatures[1]
bpm_input = 165

bpm_start = 100
step_size = 20
bpm_range = ''

if ts_input == "3/4":
    if bpm_input in range(bpm_start, bpm_start + step_size * 1):
        bpm_range = "First Set"
        # print(bpm_range)
    elif bpm_input in range(bpm_start + step_size * 1, bpm_start + step_size * 2):
        bpm_range = "Second Set"
        # print(bpm_range)
    elif bpm_input in range(bpm_start + step_size * 2, bpm_start + step_size * 3):
        bpm_range = "Third Set"
        # print(bpm_range)
    elif bpm_input in range(bpm_start + step_size * 3, bpm_start + step_size * 4):
        bpm_range = "Fourth Set"
        # print(bpm_range)
    else:
        bpm_range = "Out Of The Scope"
        # print(bpm_range)

elif ts_input == "4/4":
    if bpm_input in range(bpm_start + step_size * 1, bpm_start + step_size * 2):
        bpm_range = "4/4 First Set"
        # print(bpm_range)
    elif bpm_input in range(bpm_start + step_size * 2, bpm_start + step_size * 3):
        bpm_range = "4/4 Second Set"
        # print(bpm_range)
    elif bpm_input in range(bpm_start + step_size * 3, bpm_start + step_size * 4):
        bpm_range = "4/4 Third Set"
        # print(bpm_range)
    elif bpm_input in range(bpm_start + step_size * 4, bpm_start + step_size * 5):
        bpm_range = "4/4 Fourth Set"
        # print(bpm_range)
    else:
        bpm_range = "Out Of The Scope"
        # print(bpm_range)

