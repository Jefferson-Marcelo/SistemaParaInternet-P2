function primo(num) {
  if(num < 2){
    return false;}
  for (var i = 2; i < num; i++) {
      if(num%i==0)
          return false;
  }
  return true;
}

console.log(primo(1))