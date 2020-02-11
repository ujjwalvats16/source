//PRINT THE N TH ELEMENT FROM FIBONACCI SERIES

fn main(){
    let mut i=0;
    let mut a=0;
    let mut c=0;
    let mut b=1;
    while i<6{
    if i>1{
    c=b;
    b=b+a;
    a=c;
    i=i+1;
    }
    else {
    i=i+1;
    }
    }
    println!("{}",b);
    }
    
    //print n number of elements from fibonacci series

    fn main(){
        let mut i=0;
        let mut a=0;
        let mut c=0;
        let mut b=1;
        while i<10{
        if i>1{
        c=b;
        b=b+a;
        a=c;
        println!("{}",b);
        i=i+1;
        }
        else {
        println!("{}",i);
        i=i+1;
        }
        }
        