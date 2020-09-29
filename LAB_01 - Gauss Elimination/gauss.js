const readline = require('readline')
const math = require('mathjs')

rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

// Read from console
function input(msg) {
    return new Promise((resolve, reject) => {
        rl.question(msg, input => { 
            let val = +input 
            resolve(val)
        })
    })
}
// Output system 
function printSystem(A) {
    n = A[0].length - 1
    let str = ''
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n+1; ++j) {
            if (j != n-1 && j != n)
                str += `${A[i][j]}X${j+1} + `
            else if (j == n-1)
                str += `${A[i][j]}X${j+1} = ` 
            else if (j == n)
                str += `${A[i][j]}\n`
        }
    }   console.log(str)
}
// Calculating 
function gauss(matrix, n) {
    let res = math.zeros(n)

    for (let i = 0; i < n; ++i) {
        if (matrix[i][i] == 0) {
            process.exit(1)
        }    
        for (let j = i+1; j < n; ++j) {
            ratio = matrix[j][i]/matrix[i][i]
            
            for (let k = 0; k < n+1; ++k) {
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
            }
        }   console.log(matrix)
    }   
    // Back Substitution
    res[n-1] = matrix[n-1][n] / matrix[n-1][n-1]

    // Fill the result array
    for (let i = n-2; i > -1; --i) {
        res[i] = matrix[i][n]        
        for (let j = i+1; j < n; ++j) {
            res[i] = res[i] - matrix[i][j]*res[j]
        }
        res[i] = res[i] / matrix[i][i]
    }
    return res
}

async function main() {
    const n = await input('Enter number of unknowns: ')
    // [[1, 1, -1, 0], [2, -4, 1, 3], [1, -1, -1, -4]]
    let matrix = math.zeros(n, n+1)

    console.log('Enter Matrix Coefficients:')
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n+1; ++j) {
            matrix._data[i][j] = await input(`MATRIX[${i}][${j}]: `)
        }
    }   rl.close()

    printSystem(matrix._data)

    const resArray = gauss(matrix._data, n)
    for (let i = 0; i < n; ++i) {
        console.log(`X${i+1} = ${resArray[i].toFixed(2)}`)
    }
}

main()