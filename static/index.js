let selected_element = null;

let construct_item = (src) => {
    let image = new Image();
    image.dataset.drag = '';
    image.src = src;
    image.draggable = false;
    image.classList.add('item');
    return image;
};

let insert_element = (selected, target) => {
    selected.remove();
    if ('items' in target.dataset)
        target.append(selected);
    if ('drag' in target.dataset)
        target.parentNode.insertBefore(selected, target.nextSibling);
    if ('row' in target.dataset)
        target.children[1].append(selected);;
}

let drag_start = (e) => 'drag' in e.target.dataset ? selected_element = e.target : null;

let drag_move = (e) => {
    if (selected_element)
    {
        selected_element.style.position = 'absolute';
        selected_element.style.left = `${e.clientX + window.scrollX - selected_element.clientWidth / 2}px`;
        selected_element.style.top = `${e.clientY + window.scrollY - selected_element.clientHeight / 2}px`;
    }
}

let drag_end = (e) => {
    if (selected_element)
    {
        let target_element = document.elementsFromPoint(e.clientX, e.clientY)[1];
        if (['items', 'drag', 'row'].some((d) => d in target_element.dataset))
            insert_element(selected_element, target_element);
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

window.addEventListener('drop', (e) => {
    e.preventDefault();
    let target_element = e.target;
    if (['items', 'drag', 'row'].some((d) => d in target_element.dataset))
    {
        for (const file of e.dataTransfer.files)
        {
            let reader = new FileReader();
            reader.onload = (e) => {
                insert_element(construct_item(e.target.result), target_element);
            }
            reader.readAsDataURL(file);
        }
    }
});
window.addEventListener('dragover', (e) => { e.preventDefault(); });

let to_rank_div = document.getElementById('to-rank');

let input_images = (files) => {
    for (const file of files) 
    {
        let reader = new FileReader();
        reader.onload = (e) => { to_rank_div.append(construct_item(e.target.result)); }
        reader.readAsDataURL(file);
    }
}

document.getElementById('to-rank-input').addEventListener('input', (e) => { input_images(e.target.files) });

