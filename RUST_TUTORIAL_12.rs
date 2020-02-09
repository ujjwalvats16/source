//RUST WITHOUT BREAK

fn main(){
    loop{
    println!("this is loop example");
    }
    } 

//RUST WITH EXPLICIT BREAK
fn main(){
    let mut i=0;
    loop{
        println!("this is loop example");
        i+=1;
        if i==10{
            break;
        }
    }
    
}


