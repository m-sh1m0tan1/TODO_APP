'use strict';

const task_titles = document.getElementsByClassName('task-title');
for (let i = 0; i < task_titles.length; i++){
    // console.log(task_titles[i].innerHTML);
    let title = task_titles[i].innerHTML;
    if (title.length > 10){
        title = title.substring(0, 10) + '...';
    }
    task_titles[i].innerHTML = title;
}
