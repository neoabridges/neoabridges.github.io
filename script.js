function search() {
    const searchInput = document.getElementById('searchInput').value;
    const searchResults = document.getElementById('searchResults');
    
    // 清空以前的搜索结果
    searchResults.innerHTML = '';

    if (searchInput.trim() === '') {
        searchResults.classList.remove('visible');
        return;
    }

    // 模拟搜索结果
    let results = [
        'Banana',
        'Apple',
        'Orange',
        'Mango',
        'Pineapple',
        'Grapes',
        'Strawberry',
        'Blueberry',
        'Watermelon',
        'Lemon'
    ].filter(item => item.toLowerCase().includes(searchInput.toLowerCase()));

    // 将结果按字典序排序
    results.sort((a, b) => a.localeCompare(b));

    // 将搜索结果添加到结果容器中
    results.forEach(result => {
        const resultItem = document.createElement('div');
        resultItem.textContent = result;
        resultItem.draggable = true;
        resultItem.classList.add('draggable');
        resultItem.ondragstart = (e) => {
            e.dataTransfer.setData('text/plain', result);
            e.target.classList.add('dragging');
        };
        resultItem.ondragend = (e) => {
            e.target.classList.remove('dragging');
        };
        searchResults.appendChild(resultItem);
    });

    // 显示搜索结果容器
    if (results.length > 0) {
        searchResults.classList.add('visible');
    } else {
        searchResults.classList.remove('visible');
    }
}

// 在输入框中输入时触发搜索
document.getElementById('searchInput').addEventListener('input', search);

const explorer = document.querySelector('.explorer');
const explorerContent = document.createElement('div');
explorerContent.classList.add('explorer-content');
explorer.appendChild(explorerContent);

explorer.ondragover = (e) => {
    e.preventDefault();
    explorer.classList.add('drop-target');
};

explorer.ondragleave = (e) => {
    explorer.classList.remove('drop-target');
};

explorer.ondrop = (e) => {
    e.preventDefault();
    explorer.classList.remove('drop-target');
    
    const data = e.dataTransfer.getData('text/plain');
    if (data) {
        const ellipse = document.createElement('div');
        ellipse.textContent = data;
        ellipse.classList.add('ellipse');
        explorerContent.appendChild(ellipse);
    }
};
