const tickets = [
    { id: 1, title: 'Html', status: 'Frontend' },
    { id: 2, title: 'Css3', status: 'Frontend'},
    { id: 3, title: 'Javascript', status: 'Frontend'},
    { id: 4, title: 'Typescript', status: 'Backend'},
    { id: 5, title: 'Python', status: 'Backend'},
];

// Agrupar tickets por el status buscando similitud
const ticketsByStatus = Object.groupBy(tickets, (ticket) => ticket.status);

console.log(ticketsByStatus);