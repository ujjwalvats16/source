
fn get_value(a:Option<i32>)->Option<i32>{
    match a{
        None=>None,
        Some(a)=>Some(a+100),
    }
}

fn main(){

    let a=None;
    let x=get_value(a);

    match x{
        Option::Some(value)=>println!("value is {}",value ),
        Option::None=>println!("none value found" ),
    }
}
