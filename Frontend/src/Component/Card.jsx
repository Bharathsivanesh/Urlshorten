import React from "react";

const UrlCard = ({ urlData, onDelete }) => {
  return (
    <div className="flex justify-between items-center p-4 mb-3 bg-gray-50 border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition-shadow">
      <a
        href={urlData.Short_url}
        target="_blank"
        rel="noreferrer"
        className="text-blue-600 hover:underline break-words"
      >
        {urlData.Short_url}
      </a>
      <button
        onClick={() => onDelete(urlData.id)}
        className="px-3 py-1 bg-red-500 text-white rounded-md hover:bg-red-600 transition-colors"
      >
        Delete
      </button>
    </div>
  );
};

export default UrlCard;
