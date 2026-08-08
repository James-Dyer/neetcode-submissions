func isValidSudoku(board [][]byte) bool {
    for i := 0; i < 9; i++ {
        row := map[byte]bool{}
        col := map[byte]bool{}
        box := map[byte]bool{}

        for j := 0; j < 9; j++ {

            // row
            if v := board[i][j]; v != '.' {
                if row[v] {
                    return false
                }
                row[v] = true
            }

            // column
            if v := board[j][i]; v != '.' {
                if col[v] {
                    return false
                }
                col[v] = true
            }

            // 3x3 box
            r := (i/3)*3 + j/3
            c := (i%3)*3 + j%3

            if v := board[r][c]; v != '.' {
                if box[v] {
                    return false
                }
                box[v] = true
            }
        }
    }

    return true
}