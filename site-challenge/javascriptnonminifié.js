function resetTxtField(id)
{
    // id est l'id de la réponse avec textfield associé
    for(var i = 0; i <id.length; i++){
				console.log(id[i]);
        if(!document.getElementById(id[i]).checked)
        {
            txtfillId = id[i] + ":textfill";
            document.getElementById(txtfillId).value="";
        }
    }
}


function setFocus(id)
{
    document.getElementById(id).checked = true;
}
