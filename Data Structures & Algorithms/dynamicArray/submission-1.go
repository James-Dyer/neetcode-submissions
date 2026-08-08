type DynamicArray struct {
    data []int
    length int
    capacity int
}

func NewDynamicArray(capacity int) *DynamicArray {

    return &DynamicArray {
        data : make([]int, capacity),
        length : 0,
        capacity : capacity,
    }
}

func (da *DynamicArray) Get(i int) int {
    return da.data[i]
}

func (da *DynamicArray) Set(i int, n int) {
    da.data[i] = n
}

func (da *DynamicArray) Pushback(n int) {
    // check if capacity is reached
    if da.length == da.capacity {
        da.resize()
    }

    // push element
    da.data[da.length] = n
    da.length++
}

func (da *DynamicArray) Popback() int {
    // if da.length * 2 == da.capacity {
        
    //     new_arr := make([]int, da.capacity / 2)
    //     for i := 0; i < da.length; i++ {
    //         new_arr[i] = da.data[i]
    //     }
    //     da.data = new_arr
    //     da.capacity /= 2
    // }

    
    da.length--
    return da.data[da.length]
}

func (da *DynamicArray) resize() {
    // create larger array
    new_arr := make([]int, da.capacity * 2)
    for i, val := range da.data {
        new_arr[i] = val
    }
    da.data = new_arr
    da.capacity *= 2
}

func (da *DynamicArray) GetSize() int {
    return da.length
}

func (da *DynamicArray) GetCapacity() int {
    return da.capacity
}
