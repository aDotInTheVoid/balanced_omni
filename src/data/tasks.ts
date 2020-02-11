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
    title: 'Get on top of emails',
    priority: -2,
    importance: -2,
    urgency: 3.5,
    quadrent: 'Urgent but not important',
    dueDate: 'Jan 12',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },
  {
    id: 1,
    title: 'Maths paper',
    priority: 0.2,
    importance: 4,
    urgency: -2,
    quadrent: 'Important but not urgent',
    dueDate: 'March 6',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },
  {
    id: 2,
    title: 'Prepare trade stand',
    priority: 3,
    importance: 3,
    urgency: 3,
    quadrent: 'Important and urgent',
    dueDate: 'Feb 12',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempus massa ex, eget auctor nibh malesuada convallis.',
  },
];

export default Tasks;
