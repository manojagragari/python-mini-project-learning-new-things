function addItem() {
    const itemInput = document.getElementById('itemInput');
    const itemList = document.getElementById('itemList');
    const newItemText = itemInput.value.trim();

    if (newItemText !== '') {
        const listItem = document.createElement('li');
        listItem.textContent = newItemText;
        itemList.appendChild(listItem);
        itemInput.value = '';
    }else{
        alert("Please enter an item.");
    }
}