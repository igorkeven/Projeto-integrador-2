function exibir_formulario(tipo){
    add_autorizacao = document.getElementById('adicionar-autorizacao')
    att_autorizacao = document.getElementById('atualizar-autorizacao')
    if(tipo=="1"){
        att_autorizacao.style.display="none"
        add_autorizacao.style.display="block"
    }else if(tipo=="2"){
        add_autorizacao.style.display="none"
        att_autorizacao.style.display="block"
    }
    
}

function dados_autorizacao(){
    autorizacao = document.getElementById('autorizacao-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_autorizacao = autorizacao.value

    data = new FormData()
    data.append('id_autorizacao', id_autorizacao)

    fetch("/autorizacao/atualiza_autorizacao/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        document.getElementById('form-att-autorizacao').style.display='block'

        id = document.getElementById('id')
        id.value = data['autorizacao_id']

        categoria = document.getElementById('categoria')
        categoria.value = data['autorizacao']['categoria']

        tipo = document.getElementById('tipo')
        tipo.value = data['autorizacao']['tipo']

        numero = document.getElementById('numero')
        numero.value = data['autorizacao']['numero']

        emissao = document.getElementById('emissao')
        emissao.value = data['autorizacao']['emissao']

        validade = document.getElementById('validade')
        validade.value = data['autorizacao']['validade']

        proc_ADM = document.getElementById('proc_ADM')
        proc_ADM.value = data['autorizacao']['proc_ADM']

        tcaNum = document.getElementById('tcaNum')
        tcaNum.value = data['autorizacao']['tcaNum']

        compromitente = document.getElementById('compromitente')
        compromitente.value = data['autorizacao']['compromitente']

        cpfcnpj = document.getElementById('cpfcnpj')
        cpfcnpj.value = data['autorizacao']['cpfcnpj']

        insc_CAD = document.getElementById('insc_CAD')
        insc_CAD.value = data['autorizacao']['insc_CAD']

        endereco = document.getElementById('endereco')
        endereco.value = data['autorizacao']['endereco']

        quadra = document.getElementById('quadra')
        quadra.value = data['autorizacao']['quadra']

        lote = document.getElementById('lote')
        lote.value = data['autorizacao']['lote']

        bairro = document.getElementById('bairro')
        bairro.value = data['autorizacao']['bairro']

        area_lote = document.getElementById('area_lote')
        area_lote.value = data['autorizacao']['area_lote']

        sup_aut = document.getElementById('sup_aut')
        sup_aut.value = data['autorizacao']['sup_aut']

        matricula = document.getElementById('matricula')
        matricula.value = data['autorizacao']['matricula']

        anuencia_CETESB = document.getElementById('anuencia_CETESB')
        anuencia_CETESB.value = data['autorizacao']['anuencia_CETESB']

        anuencia_CONDEMA = document.getElementById('anuencia_CONDEMA')
        anuencia_CONDEMA.value = data['autorizacao']['anuencia_CONDEMA']

        compensacao_averbacao = document.getElementById('compensacao_averbacao')
        compensacao_averbacao.value = data['autorizacao']['compensacao_averbacao']

        observacao = document.getElementById('observacao')
        observacao.value = data['autorizacao']['observacao']

        objetivo = document.getElementById('objetivo')
        objetivo.value = data['autorizacao']['objetivo']

        local = document.getElementById('local')
        local.value = data['autorizacao']['local']

        nativos = document.getElementById('nativos')
        nativos.value = data['autorizacao']['nativos']

        exoticos = document.getElementById('exoticos')
        exoticos.value = data['autorizacao']['exoticos']

        euterpe = document.getElementById('euterpe')
        euterpe.value = data['autorizacao']['euterpe']

        transplante = document.getElementById('transplante')
        transplante.value = data['autorizacao']['transplante']

        vegetacao = document.getElementById('vegetacao')
        vegetacao.value = data['autorizacao']['vegetacao']

        estagio = document.getElementById('estagio')
        estagio.value = data['autorizacao']['estagio']

        area_aut = document.getElementById('area_aut')
        area_aut.value = data['autorizacao']['area_aut']

        recup_PRAD = document.getElementById('recup_PRAD')
        recup_PRAD.value = data['autorizacao']['recup_PRAD']

        app1 = document.getElementById('app1')
        app1.value = data['autorizacao']['app1']

        app2 = document.getElementById('app2')
        app2.value = data['autorizacao']['app2']

        reserva = document.getElementById('reserva')
        reserva.value = data['autorizacao']['reserva']

        restricao = document.getElementById('restricao')
        restricao.value = data['autorizacao']['restricao']

        area_rest = document.getElementById('area_rest')
        area_rest.value = data['autorizacao']['area_rest']
    })

}

function update_autorizacao(){
    categoria = document.getElementById('categoria').value
    tipo = document.getElementById('tipo').value
    numero = document.getElementById('numero').value
    emissao = document.getElementById('emissao').value
    validade = document.getElementById('validade').value
    proc_ADM = document.getElementById('proc_ADM').value
    tcaNum = document.getElementById('tcaNum').value
    compromitente = document.getElementById('compromitente').value
    cpfcnpj = document.getElementById('cpfcnpj').value
    insc_CAD = document.getElementById('insc_CAD').value
    endereco = document.getElementById('endereco').value
    quadra = document.getElementById('quadra').value
    lote = document.getElementById('lote').value
    bairro = document.getElementById('bairro').value
    area_lote = document.getElementById('area_lote').value
    sup_aut = document.getElementById('sup_aut').value
    matricula = document.getElementById('matricula').value
    anuencia_CETESB = document.getElementById('anuencia_CETESB').value
    anuencia_CONDEMA = document.getElementById('anuencia_CONDEMA').value
    compensacao_averbacao = document.getElementById('compensacao_averbacao').value
    observacao = document.getElementById('observacao').value
    objetivo = document.getElementById('objetivo').value
    local = document.getElementById('local').value
    nativos = document.getElementById('nativos').value
    exoticos = document.getElementById('exoticos').value
    euterpe = document.getElementById('euterpe').value
    transplante = document.getElementById('transplante').value
    vegetacao = document.getElementById('vegetacao').value
    estagio = document.getElementById('estagio').value
    area_aut = document.getElementById('area_aut').value
    recup_PRAD = document.getElementById('recup_PRAD').value
    app1 = document.getElementById('app1').value
    app2 = document.getElementById('app2').value
    reserva = document.getElementById('reserva').value
    restricao = document.getElementById('restricao').value
    area_rest = document.getElementById('area_rest').value
    id = document.getElementById('id').value

    fetch('/autorizacao/update_autorizacao/' + id, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify({
            categoria: categoria,
            tipo: tipo,
            numero: numero,
            emissao: emissao,
            validade: validade,
            proc_ADM: proc_ADM,
            tcaNum: tcaNum,
            compromitente: compromitente,
            cpfcnpj: cpfcnpj,
            insc_CAD: insc_CAD,
            endereco: endereco,
            quadra: quadra,
            lote: lote,
            bairro: bairro,
            area_lote: area_lote,
            sup_aut: sup_aut,
            matricula: matricula,
            anuencia_CETESB: anuencia_CETESB,
            anuencia_CONDEMA: anuencia_CONDEMA,
            compensacao_averbacao: compensacao_averbacao,
            observacao: observacao,
            objetivo: objetivo,
            local: local,
            nativos: nativos,
            exoticos: exoticos,
            euterpe: euterpe,
            transplante: transplante,
            vegetacao: vegetacao,
            estagio: estagio,
            area_aut: area_aut,
            recup_PRAD: recup_PRAD,
            app1: app1,
            app2: app2,
            reserva: reserva,
            restricao: restricao,
            area_rest: area_rest,
            id: id,
        })
    }).then(function(result){
        return result.json()
    }).then(function(data){
        if(data['status'] == '200'){
            console.log('Dados alterados com sucesso')
            msg = "Dados alterados com sucesso";
        }else{
            console.log('Ocorreu algum erro')
            msg = "Ocorreu algum erro";
        }
        alert(msg)
    })
}