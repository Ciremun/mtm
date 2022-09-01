let selected_element = null;

let insert_element = (selected, target, is_row) => {
    selected.remove();
    if (is_row)
        target = target.children[1];
    target.append(selected);
}

let drag_start = (e) => 'drag' in e.target.dataset ? selected_element = e.target : null;

let drag_move = (e) => {
    if (selected_element)
    {
        selected_element.style.position = 'absolute';
        selected_element.style.left = `${e.clientX - selected_element.clientWidth / 2}px`;
        selected_element.style.top = `${e.clientY - selected_element.clientHeight / 2}px`;
    }
}

let drag_end = (e) => {
    if (selected_element)
    {
        let target_element = document.elementsFromPoint(e.clientX, e.clientY)[1];
        if ('items' in target_element.dataset)
            insert_element(selected_element, target_element, false);
        else if ('row' in target_element.dataset)
            insert_element(selected_element, target_element, true);
        selected_element.style.position = null;
        selected_element.style.left = null;
        selected_element.style.top = null;
        selected_element = null;
    }
}

window.addEventListener('touchstart', drag_start);
window.addEventListener('touchmove', (e) => { drag_move(e.touches[0]); });
window.addEventListener('touchend', (e) => { drag_end(e.touches[0]); });
window.addEventListener('mousedown', drag_start);
window.addEventListener('mousemove', drag_move);
window.addEventListener('mouseup', drag_end);

let to_rank_div = document.getElementById('to-rank');

let input_images = (files) => {
    for (const file of files) 
    {
        let reader = new FileReader();
        reader.onload = function (e) {
            let image = new Image();
            image.dataset.drag = '';
            image.src = e.target.result;
            image.draggable = false;
            image.classList.add('item');
            to_rank_div.append(image);
        }
        reader.readAsDataURL(file);
    }
}

document.getElementById('to-rank-input').addEventListener('input', (e) => { input_images(e.target.files) });

