type LinkedList struct {
    head *Node
    length int
}

type Node struct {
    val int
    next *Node
}

func NewLinkedList() *LinkedList {
    return &LinkedList {}
}

func NewNode(initialValue int) *Node {
    return &Node {
        val : initialValue,
    }
}

func (ll *LinkedList) Get(index int) int {
    if index < 0 || index >= ll.length {
        return -1
    }

    curr := ll.head
    for range index {
	    curr = curr.next
    }

    return curr.val
}

func (ll *LinkedList) InsertHead(val int) {
    newNode := NewNode(val)
    newNode.next = ll.head
    ll.head = newNode
    ll.length++
}

func (ll *LinkedList) InsertTail(val int) {
    if ll.length == 0 {
        newNode := NewNode(val)
        ll.head = newNode
    }

    curr := ll.head
    for range ll.length - 1 {
        curr = curr.next
    }

    newNode := NewNode(val)
    curr.next = newNode
    ll.length++
}

func (ll *LinkedList) Remove(index int) bool {
    if index < 0 || index >= ll.length {
        return false
    }

    if index == 0 {
        ll.head = ll.head.next
        ll.length -= 1
        return true
    }

    curr := ll.head
    var prev *Node
    for range index {
        prev = curr
        curr = curr.next
    }

    // rewire prev
    prev.next = curr.next
    ll.length--
    return true

}

func (ll *LinkedList) GetValues() []int {
    curr := ll.head
    res := make([]int, ll.length)
    for i := range ll.length {
        res[i] = curr.val
        curr = curr.next
    }
    
    return res
}
