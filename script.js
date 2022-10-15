function exportBoard() {
    let anchors = document.getElementsByTagName('div');
    let board = {
        horizontalEdges : [],
        verticalEdges : [],
        squares: []
    };

    for (let i = 0; i < anchors.length; i++) {
        let anchor = anchors[i];
        if (anchor.className.includes("row-spacer")) { // rel info = horizontal lines, should be 6 of them
            let arr = [];
            for (child of anchor.children) {
                if (child.className.includes("line-h-red")) {
                    arr.push("R");
                } else if (child.className.includes("line-h-blue")) {
                    arr.push("B");
                } else if (!child.className.includes("dot")) {
                    arr.push(" ");
                }
            }
            board.horizontalEdges.push(arr);
        } else if (anchor.className.includes("row-squares")) {
            let arrSquares = [];
            let arrLines = [];

            for (child of anchor.children) {
                if (child.className.includes("square-red")) {
                    arrSquares.push("R");
                } else if (child.className.includes("square-blue")) {
                    arrSquares.push("B");
                } else if (child.className === "square") {
                    arrSquares.push(" ");
                } else if (child.className.includes("line-v-red")) {
                    arrLines.push("R");
                } else if (child.className.includes("line-v-blue")) {
                    arrLines.push("B");
                } else if (child.className === "line-v") {
                    arrLines.push(" ");
                }
            }
            board.verticalEdges.push(arrLines);
            board.squares.push(arrSquares);
        }
    }
    return board;
}

function printBoard() {
    console.log(JSON.stringify(exportBoard()));
}