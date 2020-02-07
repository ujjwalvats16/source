

//simple function

fn main(){
    write_something();
    }
    fn write_something(){
    println!("this is written by rust function");
    }
    
//with parameters
fn main(){
    write_something(5);
    }
    fn write_something(a:i32){
    println!("the value of a square is {}",a*a);
    }

//with return keyword
fn main(){

let value =write_something(5);
println!("the value is {}",value);
}

fn write_something(a:i32)->i32{
    return(a*a);
}


//without return keyword   
fn main() {
let value =write_something(5);
println!("the value is {}",value);
}
fn write_something(a:i32)->i32{
    a*a
}


