export type Task = {
    id: Number,
    title: String,
    x: Number,
    y: Number,
    z: Number,
    q: String,
    description: String
    dueDate: String
};

const Tasks: Task[] = [
  {
    id: 0,
    title: 'Taskidy Task',
    x: 2,
    y: 5,
    z: 3.5,
    q: 'Heterozygous',
    dueDate: 'Jan 12',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },
  {
    id: 1,
    title: 'Something Else',
    x: 23,
    y: 5.34,
    z: 3.432,
    q: 'Heterozygous',
    dueDate: 'Jan 43',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },
  {
    id: 2,
    title: 'Find 3.4 slugs',
    x: 3,
    y: 5,
    z: -4.2,
    q: 'Heterozygous',
    dueDate: 'Octanuary 43',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },

];

export default Tasks;
