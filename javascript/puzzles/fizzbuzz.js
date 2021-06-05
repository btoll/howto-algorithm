for (let i = 1; i <= 20; i++) {
    let fizzbuzz = 0;
//
//    s = ""
//    if (i % 3 == 0) {
//        s += "fizz"
//    }
//
//    if (i % 5 == 0) {
//        s += "buzz"
//    }
//
//    console.log(i, s)

    if (i % 3 === 0) {
        fizzbuzz = 1;
    }

    if (i % 5 === 0) {
        fizzbuzz += 2;
    }

    switch (fizzbuzz & 3) {
        case 0:
            console.log(i);
            break;
        case 1:
            console.log('fizz');
            break;
        case 2:
            console.log('buzz');
            break;
        case 3:
            console.log('fizzbuzz');
            break;
    }
}

