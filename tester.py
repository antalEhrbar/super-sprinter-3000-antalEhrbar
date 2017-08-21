def get_file_name():
    return "./templates/datas.csv"


def write_story_to_file(all_story):
    file_name = get_file_name()
    with open(file_name, "w") as file:
        for record in all_story:
            row = ';'.join(record)
            file.write(row + "\n")


def read_story_from_file():
    file_name = get_file_name()
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def add(new_story):
    stories = read_story_from_file()
    maxi = 0
    for line in stories:
        if int(line[0]) > maxi:
            maxi = int(line[0])
    new_story.insert(0, maxi)
    stories.append(new_story)
    write_story_to_file()

"""
def update():
    user_updates = ui.get_inputs(['month', 'day', 'year', 'type', 'amount'], 'For update the items')
    id_ = id_[0]
    for line in table:
        if id_ == line[0]:
            for i in range(len(user_updates)):
                line[i+1] = user_updates[i]
    data_manager.write_table_to_file('./accounting/items.csv', table)
    ui.print_result(line, "The updated list is:")
    return table
"""
id_ = "2"
new_story = [['4', 'title', 'story', 'crit', '200', '2', 'Review'], ['5', 'New Hope', 'Something, something', 'Dark side', '200', '1', 'In Progress'], ['3', 'title', 'story', 'crit', '200', '2', 'Review'], ['6', 'New Hope', 'Something, something', 'Dark side', '200', '1', 'In Progress']]
add(new_story)
#all_story = read_story_from_file()
#write_story_to_file(all_story)
