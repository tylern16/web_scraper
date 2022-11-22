import './App.css'
import {useState, useEffect} from 'react'


const jsonData = require('./data.json')
// import {jsonData} from './data.json'

function App() {
  let [teams, setTeams] = useState(jsonData)
  let groups = 0

  return (
    <div className="App">
      <h1>World Cup Standings</h1>
      <div className='container'>
        {teams.map((team, i) => {
          if (i%4 === 0) {
            return (
              <>
                <div className='grid-item'>
                  <span>Position &nbsp;</span>
                  <span>Name &nbsp;</span>    
                  <span>Wins&nbsp;</span> 
                  <span>Draws &nbsp;</span> 
                  <span>Losses &nbsp;</span>  
                  <span>Points &nbsp;</span> 
                </div>
                <div className='grid-item'>
                  <span>{team.position} &nbsp;</span>
                  <span>{team.team_name}&nbsp;</span>    
                  <span>{team.wins}&nbsp;</span> 
                  <span>{team.draws}&nbsp;</span> 
                  <span>{team.losses}&nbsp;</span>  
                  <span>{team.points}&nbsp;</span>                 
                </div>
              </>
              
            )
          } else {
            return (
              <>
                <div className='grid-item'>
                  <span>{team.position} &nbsp;</span>
                  <span>{team.team_name}&nbsp;</span>    
                  <span>{team.wins}&nbsp;</span> 
                  <span>{team.draws}&nbsp;</span> 
                  <span>{team.losses}&nbsp;</span>  
                  <span>{team.points}&nbsp;</span>            
                </div>
              </>
            )
          }
              
        })} 
      </div>
    </div>
  );
}

export default App;
