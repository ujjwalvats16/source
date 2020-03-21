
//tutorial 19

//passing string variables to a function

fn main(){

    let a =String::from("total technology");
    func_string(a);
    println!("{}",a); //error due to rust ownership rule
}
fn func_string(a_value:String){
    println!("{}",a_value);
}

//pasing integer variable to a function

fn main(){
    let b=10;
    func_int(b);
    println!("{}",b); //no error as integers are stack only data types so ownership rule will not be applicable
}



fn func_int(b_val:i32){
    println!("{}",b_val);
}