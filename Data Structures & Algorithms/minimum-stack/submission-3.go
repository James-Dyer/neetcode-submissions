type MinStack struct {
    stack [][2]int
}

func Constructor() MinStack {
    return MinStack{
		stack: make([][2]int, 0),
	}
}

func (this *MinStack) Push(val int) {
    if len(this.stack) != 0 {
        curr_min := this.stack[len(this.stack)-1][1]
        this.stack = append(this.stack, [2]int{val, min(curr_min, val)})
    } else {
        this.stack = append(this.stack, [2]int{val, val})
    }
}

func (this *MinStack) Pop() {
    this.stack = this.stack[:len(this.stack)-1]
}

func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1][0]
}

func (this *MinStack) GetMin() int {
    return this.stack[len(this.stack)-1][1]
}
