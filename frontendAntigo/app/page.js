'use client';
import { useState, useCallback } from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import { useForm, FormProvider } from 'react-hook-form';
import './header.css';
import Simulation from './Simulation';
import Networking from './Networking';
import Physical from './Physical';
import Result from './Result';

// Componente Home
function Home() {
  const navigate = useNavigate();
  const [currentPage, setCurrentPage] = useState('simulation');

  // Função para mudar a página
  const changePage = useCallback((page) => {
    setCurrentPage(page);
  }, []);

  // Função para renderizar a página atual
  const renderPage = useCallback(() => {
    switch (currentPage) {
      case 'simulation':
        return <Simulation />;
      case 'networking':
        return <Networking />;
      case 'physical':
        return <Physical />;
      default:
        return null;
    }
  }, [currentPage]);

  // Gerenciamento do formulário
  const methods = useForm();
  const onSubmit = (data) => {
    const jsonData = JSON.stringify(data, null, 2);
    console.log(jsonData);
    navigate('/result');
  };

  return (
    <main className="p-4">
      <div className="title">
        <h1 className="text-2xl font-bold mb-4">SimRoel Web</h1>
      </div>
      <div className="parameters mb-6">
        <h3 className="text-xl font-semibold mb-2">Parameters</h3>
        <div className="space-y-2">
          <button
            className={`tablinks ${currentPage === 'simulation' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            onClick={() => changePage('simulation')}
          >
            Simulation
          </button>
          <button
            className={`tablinks ${currentPage === 'networking' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            onClick={() => changePage('networking')}
          >
            Networking
          </button>
          <button
            className={`tablinks ${currentPage === 'physical' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            onClick={() => changePage('physical')}
          >
            Physical
          </button>
        </div>
      </div>
      <FormProvider {...methods}>
        <form onSubmit={methods.handleSubmit(onSubmit)}>
          {renderPage()}
          <div className="mt-4">
            <button className="bg-blue-500 text-white px-4 py-2 rounded" type="submit">
              Simulate
            </button>
          </div>
        </form>
      </FormProvider>
    </main>
  );
}

// Componente principal
export default function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/result" element={<Result />} />
        </Routes>
      </div>
    </Router>
  );
}