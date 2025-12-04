// task.js — simple client-side validation for the loginForm (username + password)

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm');
  if (!form) return; // nothing to do

  const username = document.getElementById('username');
  const password = document.getElementById('password');
  const usernameError = document.getElementById('username-error');
  const passwordError = document.getElementById('password-error');
  const formMessage = document.getElementById('form-message');

  function clearFieldError(inputEl, errorEl) {
    if (!inputEl || !errorEl) return;
    inputEl.classList.remove('input-error');
    inputEl.setAttribute('aria-invalid', 'false');
    errorEl.textContent = '';
  }

  function setFieldError(inputEl, errorEl, message) {
    if (!inputEl || !errorEl) return;
    inputEl.classList.add('input-error');
    inputEl.setAttribute('aria-invalid', 'true');
    errorEl.textContent = message;
  }

  // clear relevant error as soon as the user types
  [username, password].forEach(el => {
    if (!el) return;
    el.addEventListener('input', () => {
      const err = document.getElementById(`${el.id}-error`);
      clearFieldError(el, err);
      if (formMessage) formMessage.textContent = '';
    });
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Reset previous messages
    clearFieldError(username, usernameError);
    clearFieldError(password, passwordError);
    if (formMessage) formMessage.textContent = '';

    const valUser = username?.value?.trim() ?? '';
    const valPass = password?.value?.trim() ?? '';

    let firstInvalid = null;
    if (!valUser) {
      setFieldError(username, usernameError, 'Please enter your username.');
      firstInvalid = firstInvalid || username;
    }

    if (!valPass) {
      setFieldError(password, passwordError, 'Please enter your password.');
      firstInvalid = firstInvalid || password;
    }

    if (firstInvalid) {
      // focus the first invalid control for accessibility
      firstInvalid.focus();
      if (formMessage) formMessage.textContent = 'Please fix the errors above and try again.';
      return;
    }

    // Simulate successful login (demo only) — in production send to server
    if (formMessage) {
      formMessage.textContent = 'Success — credentials look valid (demo).';
      formMessage.classList.remove('error');
      formMessage.classList.add('success');
    }

    // For demonstration, reset the form after a short delay to show success
    setTimeout(() => form.reset(), 700);
  });
});
