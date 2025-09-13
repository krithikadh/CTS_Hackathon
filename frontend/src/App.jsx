import FormPage from './components/FunctionalComponents/FormPage'
import Results from './components/FunctionalComponents/Results'
import {BrowserRouter,Routes,Route} from 'react-router-dom'

function App() {
  return (
    <main>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<FormPage />}/>
          <Route path='/Results' element={<Results />}/>
        </Routes>
      </BrowserRouter>
    </main>
  );
}

export default App