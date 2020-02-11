export type Task = { // DONT EDIT THIS
  id: Number,
  title: String,
  priority: Number,
  urgency: Number, // Y axis
  importance: Number, // X axis
  quadrent: String,
  description: String
  dueDate: String
}

const Tasks: Task[] = [ // EDIT THIS
  {
    id: 0,
    title: 'Taskidy Task',
    priority: -0.3,
    importance: 0.5,
    urgency: 3.5,
    quadrent: 'Heterozygous',
    dueDate: 'Jan 12',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },
  {
    id: 1,
    title: 'Something Else',
    priority: 0.2,
    importance: -0.6,
    urgency: 3.432,
    quadrent: 'Heterozygous',
    dueDate: 'Jan 43',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },
  {
    id: 2,
    title: 'Find 3.4 slugs',
    priority: -0.3,
    importance: 0.8,
    urgency: -4.2,
    quadrent: 'Heterozygous',
    dueDate: 'Octanuary 43',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },
];

export default Tasks;
