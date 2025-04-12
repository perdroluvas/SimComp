// apiService.js

const API_BASE_URL = "http://localhost:8000";

// Função genérica para buscar dados (GET)
export const fetchData = async (endpoint) => {
  try {
    const response = await fetch(`${API_BASE_URL}/${endpoint}`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error(`Error fetching data from ${endpoint}:`, error);
    throw error; // Propaga o erro para ser tratado no componente
  }
};

// Função genérica para enviar dados (POST)
export const postData = async (endpoint, data) => {
  try {
    const response = await fetch(`${API_BASE_URL}/${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error(`Error posting data to ${endpoint}:`, error);
    throw error; // Propaga o erro para ser tratado no componente
  }
};

// Funções específicas para o componente Physical
export const fetchSlotSize = async () => {
  return fetchData("get_slot_size");
};

export const fetchCorePitch = async () => {
  return fetchData("get_core_pitch");
};

export const fetchNodeLoss = async () => {
  return fetchData("get_node_loss");
};

export const fetchFiberLossCoefficient = async () => {
  return fetchData("get_fiber_loss_coefficient");
};

export const fetchNoiseFigure = async () => {
  return fetchData("get_noise_figure");
};

export const fetchTrafficLambda = async () => {
  return fetchData("get_traffic_lambda");
};

export const fetchRouteAlgorithm = async () => {
  return fetchData("get_route_algorithm");
};

export const fetchPCCHoldingTime = async () => {
  return fetchData("get_pcc_holding_time");
};

export const fetchGuardBand = async () => {
  return fetchData("get_guard_band");
};

export const fetchConnHoldingTime = async () => {
  return fetchData("get_conn_holding_time");
};

export const fetchModulation = async () => {
  return fetchData("get_modulation");
};

export const fetchWavelength = async () => {
  return fetchData("get_wavelength");
};

export const fetchSpanLength = async () => {
  return fetchData("get_span_length");
};

export const fetchConfidenceInterval = async () => {
  return fetchData("get_confidence_interval");
};

export const fetchThreadNumber = async () => {
  return fetchData("get_thread_number");
};

export const fetchPCCTimeThreshold = async () => {
  return fetchData("get_pcc_time_threshold");
};

// Funções para enviar dados (POST)
export const postSlotSize = async (slotSize) => {
  return postData("set_slot_size", { slot_size: slotSize });
};

export const postCorePitch = async (corePitch) => {
  return postData("set_core_pitch", { core_pitch: corePitch });
};

export const postNodeLoss = async (nodeLoss) => {
  return postData("set_node_loss", { node_loss: nodeLoss });
};

export const postFiberLossCoefficient = async (fiberLossCoefficient) => {
  return postData("set_fiber_loss_coefficient", { fiber_loss_coefficient: fiberLossCoefficient });
};

export const postNoiseFigure = async (noiseFigure) => {
  return postData("set_noise_figure", { noise_figure: noiseFigure });
};

export const postTrafficLambda = async (trafficLambda) => {
  return postData("set_traffic_lambda", { traffic_lambda: trafficLambda });
};

export const postRouteAlgorithm = async (routeAlgorithm) => {
  return postData("set_route_algorithm", { route_algorithm: routeAlgorithm });
};

export const postPCCHoldingTime = async (pccHoldingTime) => {
  return postData("set_pcc_holding_time", { pcc_holding_time: pccHoldingTime });
};

export const postGuardBand = async (guardBand) => {
  return postData("set_guard_band", { guard_band: guardBand });
};

export const postConnHoldingTime = async (connHoldingTime) => {
  return postData("set_conn_holding_time", { conn_holding_time: connHoldingTime });
};

export const postModulation = async (modulation) => {
  return postData("set_modulation", { modulation: modulation });
};

export const postWavelength = async (wavelength) => {
  return postData("set_wavelength", { wavelength: wavelength });
};

export const postSpanLength = async (spanLength) => {
  return postData("set_span_length", { span_length: spanLength });
};

export const postConfidenceInterval = async (confidenceInterval) => {
  return postData("set_confidence_interval", { confidence_interval: confidenceInterval });
};

export const postThreadNumber = async (threadNumber) => {
  return postData("set_thread_number", { thread_number: threadNumber });
};

export const postPCCTimeThreshold = async (pccTimeThreshold) => {
  return postData("set_pcc_time_threshold", { pcc_time_threshold: pccTimeThreshold });
};