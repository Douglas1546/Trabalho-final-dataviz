// // Função para esconder todas as seções antes de mostrar a correta
// function hideAllSections() {
//     // Esconder as seções de "Num voos", "Chegada-Partida", "Rotas Principais Aeroportos" e "Mapas Principais Aeroportos"
//     document.getElementById('tab-buttons').style.display = 'none';
//     document.getElementById('Aeroporto').style.display = 'none';
//     document.getElementById('Cidade').style.display = 'none';
//     document.getElementById('chegada-partida').style.display = 'none';
//     document.getElementById('rotas-principais').style.display = 'none';
//     document.getElementById('mapas-principais').style.display = 'none';
// }

// // Função para alternar entre as abas "Aeroporto" e "Cidade" em "Num Voos"
// function openTab(evt, tabName) {
//     var i, tabcontent, tablinks;

//     // Esconder todo o conteúdo das abas
//     tabcontent = document.getElementsByClassName("tab-content");
//     for (i = 0; i < tabcontent.length; i++) {
//         tabcontent[i].style.display = "none";
//     }

//     // Remover a classe "active" de todos os botões de abas
//     tablinks = document.getElementsByClassName("tablink");
//     for (i = 0; i < tablinks.length; i++) {
//         tablinks[i].className = tablinks[i].className.replace(" active", "");
//     }

//     // Mostrar o conteúdo da aba clicada
//     document.getElementById(tabName).style.display = "block";
//     evt.currentTarget.className += " active";
// }

// // Função para mostrar as abas "Num voos" (Rotas por Aeroporto e Cidade)
// function showNumVoos() {
//     hideAllSections();  // Esconder todas as seções
//     // Mostrar as abas de "Num voos"
//     document.getElementById('tab-buttons').style.display = 'block';
//     document.getElementById('Aeroporto').style.display = 'block';
// }

// // Função para mostrar somente "Chegada-Partida"
// function showChegadaPartida() {
//     hideAllSections();  // Esconder todas as seções
//     // Exibir apenas "Chegada-Partida"
//     document.getElementById('chegada-partida').style.display = 'block';
// }

// // Função para mostrar "Rotas Principais Aeroportos" e suas abas
// function showRotasPrincipais() {
//     hideAllSections();  // Esconder todas as seções
//     // Mostrar as abas de "Rotas Principais Aeroportos"
//     document.getElementById('rotas-principais').style.display = 'block';
//     document.getElementById('Brasilia').style.display = 'block';  // Exibir Brasília por padrão
// }

// // Função para alternar entre as rotas principais por aeroporto
// function openRotasTab(evt, tabName) {
//     var i, tabcontent, tablinks;

//     // Esconder todos os gráficos de rotas principais
//     tabcontent = document.querySelectorAll("#rotas-principais .tab-content");
//     for (i = 0; i < tabcontent.length; i++) {
//         tabcontent[i].style.display = "none";
//     }

//     // Remover a classe "active" de todos os botões de abas
//     tablinks = document.querySelectorAll("#rotas-principais-buttons .tablink");
//     for (i = 0; i < tablinks.length; i++) {
//         tablinks[i].className = tablinks[i].className.replace(" active", "");
//     }

//     // Mostrar o conteúdo da aba clicada
//     document.getElementById(tabName).style.display = "block";
//     evt.currentTarget.className += " active";
// }

// // Função para mostrar "Mapas Principais Aeroportos" e suas abas
// function showMapasPrincipais() {
//     hideAllSections();  // Esconder todas as seções
//     // Mostrar as abas de "Mapas Principais Aeroportos"
//     document.getElementById('mapas-principais').style.display = 'block';
//     document.getElementById('MapaBrasilia').style.display = 'block';  // Exibir Mapa de Brasília por padrão
// }

// // Função para alternar entre os mapas principais por aeroporto
// function openMapasTab(evt, tabName) {
//     var i, tabcontent, tablinks;

//     // Esconder todos os gráficos de mapas principais
//     tabcontent = document.querySelectorAll("#mapas-principais .tab-content");
//     for (i = 0; i < tabcontent.length; i++) {
//         tabcontent[i].style.display = "none";
//     }

//     // Remover a classe "active" de todos os botões de abas
//     tablinks = document.querySelectorAll("#mapas-principais-buttons .tablink");
//     for (i = 0; i < tablinks.length; i++) {
//         tablinks[i].className = tablinks[i].className.replace(" active", "");
//     }

//     // Mostrar o conteúdo da aba clicada
//     document.getElementById(tabName).style.display = "block";
//     evt.currentTarget.className += " active";
// }

// // Exibir a aba inicial "Rotas por Aeroporto" por padrão
// document.getElementById('Aeroporto').style.display = 'block';