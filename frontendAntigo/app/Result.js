//Pagina para os resultados
import React from 'react';
import './header.css';
import { useNavigate } from 'react-router-dom';

export default function Result(){
  //Necessário para navegação 55
  const navigate = useNavigate();
  const renderHome=()=>{
    navigate('/');
  }
    return(
    <main>
      <div className="title">
        <h1>SimRoel Web</h1>
      </div>
         <div className="parameters">
            <h3>Result</h3>
         </div>
         <div>
          <button className='Button' onClick={renderHome}>Return to Parameters</button>
         </div>
     </main>
    )
}