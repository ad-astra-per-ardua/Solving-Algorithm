const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    append(data) {
        let newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.tail.next = this.head; // 원형 연결 리스트 구현
    }

    rotate() {
        this.head = this.head.next;
        this.tail = this.tail.next;
    }

    removeFirst() {
        if (!this.head) {
            return null;
        } else {
            let dataToReturn = this.head.data;
            if (this.head === this.tail) {
                this.head = null;
                this.tail = null;
            } else {
                this.head = this.head.next;
                this.tail.next = this.head;
            }
            return dataToReturn;
        }
    }
}

rl.on('line', (line) => {
    let n = parseInt(line);
    let list = new LinkedList();

    for (let i = 1; i <= n; i++) {
        list.append(i);
    }

    while (list.head !== list.tail) {
        list.removeFirst();
        list.rotate();
    }
    console.log(list.head.data);

    rl.close();
}).on('close', function () {
    process.exit();
});
