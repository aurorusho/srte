let questions = document.getElementsByClassName('question');


function manualRegex(text){
    text = text.trim();
    let lst = text.split(' ');
    let newLst = new Array();

    for(let i = 0; i < lst.length; i++){
        item = lst[i];
        let endCond = item.endsWith('_') || item.endsWith('_,');
        endCond = endCond || item.endsWith('_.') || item.endsWith('_:');
        if(item.startsWith('_') && endCond){
            newLst.push(item);
        
        }
    }
    return newLst;
}

function underline(){
    for(let i = 0; i < questions.length; i++){
        let question = questions[i];
        let answerLst = manualRegex(question.innerHTML);
        
        for(let ai = 0; ai < 4; ai++){
            let answer = answerLst[ai].replaceAll('_', '');
            answer = answer.replaceAll('#', ' ');
            let newB = document.createElement('b');
            newB.innerHTML = answer;
            newB.className = 'underline';

            question.innerHTML = question.innerHTML.replace(
                answerLst[ai], newB.outerHTML
            )
        }
        question.innerHTML = (i + 1) + '.- ' + question.innerHTML;
    }
    document.getElementById('hide').style = "display:contents";
}

function underlineAndLabel(){
    for(let i = 0; i < questions.length; i++){
        let question = questions[i];
        let answerLst = manualRegex(question.innerHTML);
        for(let ai = 0; ai < 4; ai++){
            switch(ai){
                case 0:
                    ansLetter = 'A';
                    break;
                case 1:
                    ansLetter = 'B';
                    break;
                case 2:
                    ansLetter = 'C';
                    break;
                case 3:
                    ansLetter = 'D';
                    break;
            }
            
            let answer = answerLst[ai].replaceAll('_', '');
            answer = answer.replaceAll('#', ' ');
            let newLabel = document.createElement('label');
            newLabel.setAttribute('for', ansLetter + question.id);
            
            newLabel.innerHTML = answer;
            newLabel.className = 'underline';

            question.innerHTML = question.innerHTML.replace(
                answerLst[ai], newLabel.outerHTML
            )
        }
        question.innerHTML = (i + 1) + '.- ' + question.innerHTML;
    }
    document.getElementById('hide').style = "display:contents";
}